train_out = []
train_in = []
passenger = []

for i in range(10):
  Out, In = map(int, input().split())
  train_out.append(Out)
  train_in.append(In)

passenger.append(train_in[0])

for i in range (9):
  passenger.append(passenger[i]-train_out[i+1]+train_in[i+1])

print(max(passenger))