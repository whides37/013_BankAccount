# 目的
- 100時間勉強、公式問題集完璧に理解した（つもり）。
- それでも資格試験受験→不合格。
- 自分に足りていない部分を補うために小さいアプリを作って→printしまくることに！

# 勉強法
- AIに苦手分野を伝えて→AIの出した仕様に沿って、コードを書く。
- わからないところはAIのサポートに頼る。
- ただし、すべてのコードをノートに再度書き写して、コードの理解を深める。

## 仕様

### クラス
    BankAccount

### 属性
    name（口座名義）
    balance（初期値0）

### メソッド
    deposit(amount)
        0以下なら ValueError
        正常なら残高加算
    withdraw(amount)
        0以下なら ValueError
        残高不足なら ValueError
        正常なら減算

    transfer(other_account, amount)
        other_account が BankAccount型じゃなければ TypeError
        amountが不正なら ValueError
        成功したら振込

    get_balance()

## 追加仕様

### 利率計算メソッド
    def apply_interest(rate):
        rateが0なら ZeroDivisionError をわざと起こす処理を入れる
        rateが負なら ValueError
        正常なら balance * rate を加算
        ※ZeroDivisionErrorは自分でraiseしてもいいし、0除算起こしてもOK