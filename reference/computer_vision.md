# Azure Computer Vision
- ドキュメント:クイックスタートを詳細をしっかり読む
  - Azure 関連はドキュメントがしっかりしている
> https://docs.microsoft.com/ja-jp/azure/cognitive-services/computer-vision/quickstarts-sdk/image-analysis-client-library?tabs=visual-studio&pivots=programming-language-python
### 1. Azure portal で Computer Vision リソースを作成
### 2. 必要なモノを import
### 3. KEY, ENDPOINT は、 secret.jsonで管理
### 4. クライアントを認証する
- Computer Vision API  (大本のドキュメント) : パラメーター(引数)
> https://westcentralus.dev.cognitive.microsoft.com/docs/services/computer-vision-v3-2/operations/56f91f2e778daf14a499f21b
- GitHub code sample
> https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/python/ComputerVision/ImageAnalysisQuickstart.py
  - ドキュメントから、辿っていって、 github で code の答えを見つけた
  - command + f で site 内検索を利用
## DetectedObject' object has no attribute 'object'
### 上記の error 発生
- JSON のアトリビュートが変更していた…
  - GitHub でライブラリ source code で確認
> https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/cognitiveservices/azure-cognitiveservices-vision-computervision
1. DetectedObject をコピー
2. 上記の repository seach で検索
3. site 内検索で検索
4. object_property というらしきもの発見
  - name が変更していた
