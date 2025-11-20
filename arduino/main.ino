// ピン設定（GPIO番号はArduinoのデジタルピンに合わせて変更）
const int SOL_PIN = 2;    // ソレノイド制御ピン
const int HALF_PIN = 3;   // カメラ半押し（AF/露出）
const int FULL_PIN = 4;   // カメラ全押し（シャッター）

// 時間設定（ミリ秒）
const int TSOL = 50;      // ソレノイド開放時間
const int TS = 10;        // シャッターON/OFF時間
const int TDELAY = 200;   // 水滴落下後のシャッター遅延
const int TWAKEUP = 500;  // カメラ起動待機
const int TWAIT = 8000;   // 次の撮影までの待機

void setup() {
  pinMode(SOL_PIN, OUTPUT);
  pinMode(HALF_PIN, OUTPUT);
  pinMode(FULL_PIN, OUTPUT);

  // 初期状態をLOWに設定
  digitalWrite(SOL_PIN, LOW);
  digitalWrite(HALF_PIN, LOW);
  digitalWrite(FULL_PIN, LOW);
}

void loop() {
  // カメラ半押しでウェイクアップ
  digitalWrite(HALF_PIN, HIGH);
  delay(TWAKEUP);

  // ソレノイドON → 水滴落下
  digitalWrite(SOL_PIN, HIGH);
  delay(TSOL);
  digitalWrite(SOL_PIN, LOW);

  // 水滴落下後の遅延
  delay(TDELAY);

  // シャッター全押し
  digitalWrite(FULL_PIN, HIGH);
  delay(TS);
  digitalWrite(FULL_PIN, LOW);

  // 半押し解除
  digitalWrite(HALF_PIN, LOW);

  // 次の撮影まで待機
  delay(TWAIT);
}