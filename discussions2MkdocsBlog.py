# -*- coding:utf-8 -*-
# vim:et:ts=4:sw=4:
#!/usr/bin/env python

import argparse
import requests
import os
import json
from slugify import slugify
from pathlib import Path

def stop_err(msg):
    sys.stderr.write('%s\n' % msg)
    sys.exit()

def gen_discussions_query(owner, repo_name, perPage, endCursor, first_n_threads):
    after_endCursor = ""
    if endCursor:
        after_endCursor = 'after: "%s"' % endCursor
    
    return f"""
    query {{
        repository(owner: "{owner}", name: "{repo_name}") {{
            discussions(
                orderBy: {{field: CREATED_AT, direction: DESC}}
                first: {perPage}
                {after_endCursor}) {{
                    nodes {{
                        title
                        number
                        url
                        createdAt
                        lastEditedAt
                        updatedAt
                        body
                        bodyText
                        bodyHTML
                        author {{
                            login
                        }}
                        category {{
                            name
                        }}
                        labels (first: 100) {{
                            nodes {{
                                name
                            }}
                        }} 
                        comments(first: {first_n_threads}) {{
                            nodes {{
                                body
                                author {{
                                    login
                                }}
                            }}
                        }}
                    }} # end nodes
                    pageInfo {{
                        hasNextPage
                        endCursor
                    }}
            }} # end discussions    
        }} # end discussions
    }} # end query
    """

def get_discussions(query, url, headers):
    response = requests.post(url, json={"query": query}, headers=headers)
    data = response.json()
    if data['data']['repository']['discussions'] is None:
        return ""
    else:
        return data['data']['repository']['discussions']

def __main__():
    parser = argparse.ArgumentParser(description="Fetch GitHub discussions data to mkdocs blog")
    parser.add_argument('-r', '--github_repo', help="GitHub repository name with namespace")
    parser.add_argument('-t', '--github_token', help='GitHub access token.')
    parser.add_argument('-o', '--outdir', help='Output directory.')
    args = parser.parse_args()

    gh_token = args.github_token
    gh_repo  = args.github_repo

    categoriesWhitelist = ['乱弹', '好玩', '资讯']

    gh_owner     = gh_repo.split("/")[0]
    gh_repo_name = gh_repo.split("/")[-1]

    # 创建目录; 目录存在则先删除 md
    outdir = args.outdir if args.outdir else os.getcwd()
    if os.path.exists(outdir):
        for file_path in Path(outdir).glob("*.md"):
            file_path.unlink()
    else:
        os.makedirs(outdir)

    url = "https://api.github.com/graphql"
    headers = {"Authorization": f"Bearer %s" % gh_token}

    hasNextPage    = True
    allDiscussions = []
    endCursor      = ""  
    while hasNextPage:
        query          = gen_discussions_query(gh_owner, gh_repo_name, 5, endCursor, 10)
        results        = get_discussions(query, url, headers)
        discussions    = results['nodes']
        hasNextPage    = results['pageInfo']['hasNextPage']
        endCursor      = results['pageInfo']['endCursor']
        allDiscussions = allDiscussions + discussions

    for discussion in sorted(allDiscussions, key=lambda x: x['number']): #fix me
        if not discussion:
            print("Null discussion!")
            continue
        discussion_title        = discussion['title']
        discussion_number       = discussion['number']
        discussion_url          = discussion['url']
        discussion_createdAt    = discussion['createdAt']
        discussion_lastEditedAt = discussion['lastEditedAt'] if discussion['lastEditedAt'] else 'None'
        discussion_updatedAt    = discussion['updatedAt']
        discussion_body         = discussion['body']
        discussion_author       = discussion['author']['login']
        discussion_category     = discussion['category']['name'].split()[-1]
        discussion_labels       = [label['name'] for label in discussion['labels']['nodes']] if discussion['labels']['nodes'] else []

        if not discussion_category in categoriesWhitelist:
            continue
        
        md_filename = slugify(discussion_title, allow_unicode=True, lowercase=False)+".md"

        metadata = "---\ntitle: %s\nnumber: %s\nurl: %s\ndate: %s\ncreatedAt: %s\nlastEditedAt: %s\nupdatedAt: %s\nauthors: [%s]\ncategories: \n  - %s\nlabels: %s\nfilename: %s\n---\n\n" % (
                    discussion_title,
                    str(discussion_number),
                    discussion_url,
                    discussion_createdAt[0:10],
                    discussion_createdAt,
                    discussion_lastEditedAt,
                    discussion_updatedAt,
                    discussion_author,
                    discussion_category,
                    discussion_labels,
                    md_filename)

        comments = f"""
<script src="https://giscus.app/client.js"
    data-repo="shenweiyan/Knowledge-Garden"
    data-repo-id="R_kgDOKgxWlg"
    data-mapping="number"
    data-term="{discussion_number}"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        """
        
        saved_md_file = os.path.join(outdir, md_filename)
        with open(saved_md_file, "w") as MD:
            MD.write(metadata)
            MD.write(discussion_body)
            MD.write(comments)       

if __name__ == "__main__":
    __main__()
