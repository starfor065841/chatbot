# chatbot
簡易pchome24h網路商場之爬蟲
並具有簡易商品過慮及搜尋最便宜商品之功能
## FSM
![alt tag](https://github.com/starfor065841/chatbot/blob/master/fsm.png?raw=true)
## How to chat with bot
## user state
為initial state，沒有特殊功能
## state1
>輸入  "開始使用"
>回應  "請輸入商品名稱"
>輸入商品後進入state2
## state2
>回應  "共幾項商品" 有時候可能因商品數過多須稍等一會
>此階段會用到爬蟲
>爬蟲搜尋時會依據所輸入的名稱與爬到的商品名稱進行對比
>準確率須達到0.7以上才納入
>輸入  "最便宜"  進入state3
>輸入  "預覽"  進入state4
>輸入  "列表"  進入state5
## state3
>依據state2納入之商品進行排序，回應價格最低商品之名稱 價格 網址 商品簡介
>回到state2
## state4
>回應經state3搜尋到商品的圖
>若未經state3則另外回應
回到state2
## state5
>回應商品的第1頁網址
>回到state2

