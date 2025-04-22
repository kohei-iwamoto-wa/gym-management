## CICDパイプラインの設計

### 概要

GitHubのmainブランチへのpushをトリガーにイメージのビルドとECSのイメージを更新する。

![CICDパイプライン](./CICDパイプライン.png)


### 使用リソース

* GitHub
* Codepipeline
* CodeBuild
* CodeDeploy