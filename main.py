from pushbullet import Pushbullet

API_KEY ="o.Zjwgv7YfvjP3WsNhI4WxqDQQGFxE7Cnq"
file = "medicine.txt"

with open(file, mode='r') as f:
  text = (f.read())

pb = Pushbullet(API_KEY)
push = pb.push_note('Please remember', text)

