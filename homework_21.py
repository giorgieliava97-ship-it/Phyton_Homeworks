# დაწერეთ ფუნქცია, რომელსაც პარამეტრად გადაეცემა რიცხვი და შეამოწმებს ეს რიცხვი არის თუ არა მარტივი
# შემდეგ ნაკადების გამოყენებით გაუშვით ეს ფუნქცია პარალელურად რომ შეამოწმოს შემდეგ ლისტში
# num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51] ყველა რიცხვი და დააბრუნოს პასუხი


import threading


def check_prime(n: int, results: dict):
  
  if n <= 1:
    results[n] = False
    return

  is_prime = True
  for i in range(2, n):
    if n % i == 0:
      is_prime = False
      break  

  results[n] = is_prime


num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51]
results = {}
threads = []


for num in num_list:
  t = threading.Thread(target=check_prime, args=(num, results))
  threads.append(t)
  t.start()


for t in threads:
  t.join()

for num in num_list:
  if results[num]:
    print(f"{num} is prime")
  else:
    print(f"{num} is not prime")

# print(results)