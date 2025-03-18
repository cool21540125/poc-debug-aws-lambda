# Note

- 2025/03/18

- https://www.youtube.com/watch?v=RDzFA8ssAws&list=PLHsofw25VEfR3Sc1Hi5i7WOvvrDGcnAbu&index=1
  - 只有講一個重點:
    - 在本地使用 VSCode debug Lambda 的時候, 如何設定 VSCode 的 launch.json
      - payload 可使用 payload.json 或 payload.path
      - 此為 VSCode debug Lambda `direct invoke`
- https://www.youtube.com/watch?v=pHFS-YrX_KQ&list=PLHsofw25VEfR3Sc1Hi5i7WOvvrDGcnAbu&index=2
  - 講兩個重點:
    - 1. 使用 `AWS Infrastructure Composer` 使用 UI 的方式拉出一個架構 (生成 CloudFormation Template)
      - template 會同步到 local filesystem 的 template.yaml
      - 並且自動生成必要的檔案及資料夾 Cool~
      - 操作方式: Create project -> Menu -> Local sync activated -> (然後選擇本地沒有 CF Template 的資料夾), 同意以後, 就可以開始拉 UI (同時異動 template)
    - 2. 使用 VSCode launch.json 設定使用 invokeTarget.target: template 的方式做 debug
      - 此為 VSCode debug Lambda `Template-based Lambda invoke`
- https://www.youtube.com/watch?v=y3ZfoCZ_yzg&list=PLHsofw25VEfR3Sc1Hi5i7WOvvrDGcnAbu&index=3
  - 有幾個重點:
    - 1. 使用 `AWS Infrastructure Composer` 開啟一個已存在的 CloudFormation project
      - 操作方式: Create project -> Menu -> Open project folder

# 缺少了

- Lambda Layers
- requirements.txt
