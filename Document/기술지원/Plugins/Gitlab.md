# [A203] Mattermost - Gitlab Plugin

## Mattermost slash commands

https://docs.gitlab.com/ee/user/project/integrations/mattermost_slash_commands.html

- `/gitlab connect` - Connect your Mattermost account to your GitLab account
- `/gitlab disconnect` - Disconnect your Mattermost account from your GitLab account
- `/gitlab todo` - Get a list of unread messages and merge requests awaiting your review
- `/gitlab subscribe list` - Will list the current channel subscriptions
- `/gitlab subscribe owner[/repo] [features]` - Subscribe the current channel to receive notifications about opened merge requests and issues for a group or repository`features` is a comma-delimited list of one or more the following:issues - includes new and closed issuesmerges - includes new and closed merge requestspushes - includes pushesissue_comments - includes new issue commentsmerge_request_comments - include new merge-request commentspipeline - include pipelinetag - include tag creationpull_reviews - includes merge request reviewslabel:"<labelname>" - must include "merges" or "issues" in feature list when using a labelDefaults to "merges,issues,tag"
- `/gitlab unsubscribe owner/repo` - Unsubscribe the current channel from a repository
- `/gitlab me` - Display the connected GitLab account
- `/gitlab settings [setting] [value]` - Update your user settings`setting` can be "notifications" or "reminders"`value` can be "on" or "off"



Mattermost 채널에서 바로 입력하는 것으로 별도의 설치 없이 (원래는 설치를 해야 하지만 SSAFY Mattermost 서버에 이미 설치가 되어 있는 것으로 보인다.) Gitlab 플러그인을 이용할 수 있다.

1. 

```
/gitlab connect
```

연결 커맨드를 입력하면 깃랩 로그인 창이 뜬다. 팀장의 계정으로 연결한다.



2. 

```
/gitlab subscribe <owner>[/<repo]
```

처음엔 이게 조금 헷갈렸는데 owner 개념 때문이었다. 여태까지 내 레포지토리는 항상 내가 owner였기 때문에 내 아이디를 입력해야 하는건가 생각했는데 그게 아니었다. 제대로 된 확인 방법은 아래와 같다.

`Settings` -> `Integrations` -> **Mattermost slash commands**



![Screen Shot 2021-08-30 at 20.24.48](Gitlab.assets/Screen Shot 2021-08-30 at 20.24.48.png)



**Display name**이 Gitlab / owner / repo 의 형태이다. 따라서 뒤에서 두번째부터 입력하면 된다.

![Screen Shot 2021-08-30 at 20.26.04](Gitlab.assets/Screen Shot 2021-08-30 at 20.26.04.png)

입력예시

```
/gitlab subscribe s05-bigdata-dist/S05P21A203
```



##### 연결이 완료되었다.