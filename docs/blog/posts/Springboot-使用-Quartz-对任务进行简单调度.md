---
title: Springboot 使用 Quartz 对任务进行简单调度
number: 43
url: https://github.com/byronlau/Knowledge-Garden/discussions/43
date: 2023-11-02
createdAt: 2023-11-02T05:03:49Z
lastEditedAt: None
updatedAt: 2023-11-02T05:03:51Z
authors: [byronlau]
categories: 
  - Java
labels: []
filename: Springboot-使用-Quartz-对任务进行简单调度.md
---

# Quartz 的简单介绍和使用

`Quartz` 是一个开源的 `Java` 调度框架，可以用来实现在指定的时间或时间间隔触发任务执行的功能。以下是使用 `Quartz` 的主要方式和基本概念。
<!-- more -->
## 基本概念

1. **Job**：需要执行的任务，可以是任何 `Java` 类，只需实现 `org.quartz.Job` 接口。
2. **JobDetail**：用于描述 `Job` 的实例，包括 `Job` 的各种属性信息。
3. **Trigger**：定义 `Job` 的触发规则，决定何时执行任务。
4. **Scheduler**：`Quartz` 的核心组件，负责管理和协调所有 `Trigger` 和 `Job` 的调度。

## 使用步骤

1. 定义一个 `Job` 类：该类需要实现 `org.quartz.Job` 接口，并重写其中的 `execute` 方法，定义需要执行的任务逻辑。
2. 创建一个 `JobDetail` 实例：该实例用于绑定 `Job` 类，以便 `Quartz` 框架能够找到并执行它。
3. 创建一个 Trigger 实例：该实例定义了 Job 的触发规则，包括触发时间、频率等。
4. 将 `JobDetail` 和 `Trigger` 注册到 `Scheduler` 中，`Scheduler` 是 `Quartz` 的核心组件，负责调度和执行任务。

## 代码示例

> 本次 Demo 根据业务不需要没有做 `Cron`表达式的兼容，后期补充

### 1.导入依赖

```xml
<dependency>
    <groupId>org.quartz-scheduler</groupId>
    <artifactId>quartz</artifactId>
    <version>2.3.2</version>
</dependency>
```

或者

```java
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-quartz</artifactId>
</dependency>
```

### 2. 定义 Job 类

```java
package com.byron.quartz;

import cn.hutool.json.JSONUtil;
import org.quartz.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import com.byron.quartz.exception.CustomException;
import javax.annotation.Resource;

/**
 * @Author: byron
 * @Date: 2023/10/16/17:26
 * @Description: 自定义任务类用于执行定时任务业务逻辑
 */
public class CustomJob implements Job {
    private static final Logger log = LoggerFactory.getLogger(CustomJob.class);

    @Resource
    private ScheduleTaskService scheduleTaskService;
    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        try {
            log.info("任务调度开始执行{}", JSONUtil.toJsonStr(context));
        } catch (Exception e) {
            // 抛出自定义异常
            throw new CustomException(e);
        }
    }
}
```

### 3. 定义调度中心类

```java
package com.byron.quartz;
import cn.hutool.core.date.DateUtil;
import com.byron.quartz.exception.CustomException;
import org.apache.commons.lang3.StringUtils;
import org.quartz.*;
import org.quartz.impl.matchers.GroupMatcher;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;
import javax.annotation.Resource;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Set;

@Service
public class ScheduleManager {

    public static final Logger log = LoggerFactory.getLogger(ScheduleManager.class);
    // 任务调度
    @Resource
    private Scheduler scheduler;

    /**
     * 开始执行任务
     */
    public void startJob(Class<? extends Job> jobClass, String jobName, String jobGroup, Integer type, Date timeConfig, JobDataMap jobDataMap) throws Exception {
        //查到信息进行修改操作  查不到进行新增操作
        String jobInfo = getJobInfo(jobName, jobGroup);
        if (StringUtils.isBlank(jobInfo)) {
            startJob(scheduler, jobClass, jobName, jobGroup, type, timeConfig, jobDataMap);
        } else {
            modifyJob(jobName, jobGroup, type, timeConfig);
        }
    }

    /**
     * 获取Job信息
     */
    public String getJobInfo(String name, String group) throws Exception {
        TriggerKey triggerKey = new TriggerKey(name, group);
        Trigger trigger = scheduler.getTrigger(triggerKey);
        if (null == trigger) {
            return null;
        }
        return String.format("time:%s,state:%s", DateUtil.format(trigger.getStartTime(), "yyyy-MM-dd HH:mm:ss"),
                scheduler.getTriggerState(triggerKey).name());
    }

    /**
     * 修改某个任务的执行时间
     */
    public boolean modifyJob(String name, String group, Integer type, Date timeConfig) throws SchedulerException {
        TriggerKey triggerKey = new TriggerKey(name, group);
        Trigger trigger = scheduler.getTrigger(triggerKey);
        Date oldStartTime = trigger.getStartTime();
        Date currentTime = new Date();
        if (type == 0) {// 立即执行
            JobKey jobKey = new JobKey(name, group);
            scheduler.triggerJob(jobKey);
            return true;
        } else { // 定时执行
            if (timeConfig.after(currentTime) || timeConfig.equals(currentTime)) {
                Trigger newTrigger = TriggerBuilder.newTrigger()
                        .withIdentity(name, group)
                        .startAt(timeConfig)
                        .build();
                scheduler.rescheduleJob(triggerKey, newTrigger);
                return true;
            }
        }
        return false;
    }

    /**
     * 删除某个任务
     */
    public void deleteJob(String name, String group) throws Exception {
        JobKey jobKey = new JobKey(name, group);
        JobDetail jobDetail = scheduler.getJobDetail(jobKey);
        if (jobDetail == null)
            return;
        scheduler.deleteJob(jobKey);
    }


    private void startJob(Scheduler scheduler, Class<? extends Job> jobClass, String jobName, String
            jobGroup, Integer type, Date timeConfig, JobDataMap dataMap) throws SchedulerException {
        // 1.创建任务
        JobDetail jobDetail = JobBuilder.newJob(jobClass).withIdentity(jobName, jobGroup).usingJobData(dataMap).build();
        if (type == 0) {
            // 立即执行
            // 2.创建触发器
            Trigger trigger = TriggerBuilder.newTrigger().withIdentity(jobName, jobGroup).startNow().build();
            scheduler.scheduleJob(jobDetail, trigger);
        } else {
            if (timeConfig.after(new Date())) {
                // 2.创建触发器
                Trigger trigger = TriggerBuilder.newTrigger().withIdentity(jobName, jobGroup).startAt(timeConfig).build();
                scheduler.scheduleJob(jobDetail, trigger);
            } else {
                throw new CustomException(jobName + "时间已经过期，任务无法执行");
            }

        }

    }

    /**
     * 暂停某个任务
     */
    public void pauseJob(String jobName, String group) throws Exception {
        JobKey jobKey = JobKey.jobKey(jobName, group);
        JobDetail jobDetail = scheduler.getJobDetail(jobKey);
        if (jobDetail == null) return;
        scheduler.pauseJob(jobKey);
    }
     /**
     * 列出所有任务
     */
    public Object listScheduleJob() throws Exception {
        GroupMatcher<JobKey> matcher = GroupMatcher.anyJobGroup();
        Set<JobKey> jobKeys = null;
        List<QuartzJobsVO> jobList = new ArrayList();
        try {
            jobKeys = scheduler.getJobKeys(matcher);
            for (JobKey jobKey : jobKeys) {
                List<? extends Trigger> triggers = scheduler.getTriggersOfJob(jobKey);
                for (Trigger trigger : triggers) {
                    QuartzJobsVO job = new QuartzJobsVO();
                    job.setJobName(jobKey.getName());
                    job.setJobGroup(jobKey.getGroup());
                    job.setJobTrigger("触发器:" + trigger.getKey());
                    Trigger.TriggerState triggerState = scheduler.getTriggerState(trigger.getKey());
                    job.setStatus(triggerState.name());
                    if (trigger instanceof SimpleTrigger) {
                        SimpleTrigger simpleTrigger = (SimpleTrigger) trigger;
                        Date startTime = simpleTrigger.getStartTime();
                        String time = DateUtil.format(startTime, "yyyy-MM-dd HH:mm:ss");
                        job.setTimeOrCronConfig(time);
                    }
                    if (trigger instanceof CronTrigger) {
                        CronTrigger cronTrigger = (CronTrigger) trigger;
                        String cronExpression = cronTrigger.getCronExpression();
                        job.setTimeOrCronConfig(cronExpression);
                    }
                    jobList.add(job);
                }
            }

        } catch (SchedulerException e) {
            e.printStackTrace();
        }
        return jobList;
    }
}
```

### 4. 定义列表视图对象 `QuartzJobsVO` 类

```java
package com.byron.quartz;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import lombok.Data;

/**
 * @Author: byron
 * @Date: 2023/10/21/13:48
 * @Description:
 */
@Data
// 对返回结果字段自定义排序
@JsonPropertyOrder({"jobName", "jobGroup", "jobTrigger", "timeOrCronConfig", "status"})
public class QuartzJobsVO {
    private String jobName;
    private String timeOrCronConfig;
    private String jobGroup;
    private String status;
    private String jobTrigger;
}
```

### 5. 服务重启加载库中未执行的任务

```java
package com.byron.quartz;

import cn.hutool.json.JSONUtil;
import com.byron.entity.TaskSchedule;
import com.byron.service.ScheduleTaskService;
import org.quartz.JobDataMap;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;
import javax.annotation.PostConstruct;
import javax.annotation.Resource;
import java.util.Date;
import java.util.List;

/**
 * @Author: byron
 * @Date: 2023/10/17/10:38
 * @Description: 启动项目时加载所有未执行的任务
 */
@Component
public class LoadTask {

    public static final Logger log = LoggerFactory.getLogger(LoadTask.class);

    @Resource
    private ScheduleManager quartzManager;

    @Resource
    private ScheduleTaskService scheduleTaskService;

    @PostConstruct
    public void initSchedule() {

        try {
            //从表里获取有效的任务并启动
            List<TaskSchedule> validScheduleTaskList = scheduleTaskService.getValidScheduleTask();
            log.info("有效任务开始加载{}", JSONUtil.toJsonStr(validScheduleTaskList));
            for (TaskSchedule taskSchedule : validScheduleTaskList) {
                String taskId = taskSchedule.getTaskId();
                String jobName = taskSchedule.getJobName();
                String jobGroup = taskSchedule.getJobGroup();
                Date timeConfig = taskSchedule.getTimeConfig();
                Integer type = taskSchedule.getType();
                JobDataMap dataMap = new JobDataMap();
                dataMap.put("taskId", taskId);
                quartzManager.startJob(CustomJob.class, jobName, jobGroup, type, timeConfig, dataMap);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### 6. 启动任务

> 需要在启动类上加入`@EnableScheduling` 注解

```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
@EnableScheduling
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

未完待续...

<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="43"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        