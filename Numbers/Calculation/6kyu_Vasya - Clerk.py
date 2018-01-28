"""
Description:
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?

Return YES, if Vasya can sell a ticket to each person and give the change with the bills he has at hand at that moment. Otherwise return NO.

###Examples:

### Python ###

tickets([25, 25, 50]) # => YES 
tickets([25, 100]) 
         # => NO. Vasya will not have enough money to give change to 100 dollars

"""




def tickets(people):
    cashbox = {100: 0, 50: 0, 25: 0}
    answer = 'NO'
    
    for i in people:
        if i == 25:
            cashbox[25] += 1
        elif i == 50:
            if cashbox[25] == 0:
                break
            cashbox[50] += 1
            cashbox[25] -= 1
        elif i == 100:
            if cashbox[50] == 0 and cashbox[25] <= 2 or cashbox[50] != 0 and cashbox[25] == 0:
                break
            elif cashbox[50] == 0 and cashbox[25] > 2:
                cashbox[25] -= 3
            else:
                cashbox[100] += 1
                cashbox[50] -= 1
                cashbox[25] -= 1
    else:
        answer = 'YES'
        
    return answer









def tickets(people):
  till = {100.0:0, 50.0:0, 25.0:0}

  for paid in people:
    till[paid] += 1
    change = paid-25.0
    
    for bill in (50,25):
      while (bill <= change and till[bill] > 0):
        till[bill] -= 1
        change -= bill

    if change != 0:
      return 'NO'
        
  return 'YES'














test.assert_equals(tickets([25, 25, 50]), "YES")
test.assert_equals(tickets([25, 100]), "NO")
test.assert_equals(tickets([25, 25, 25, 25, 25, 25, 25, 25, 25, 25]), "YES")
test.assert_equals(tickets([50, 50, 50, 50, 50, 50, 50, 50, 50, 50]), "NO")
test.assert_equals(tickets([100, 100, 100, 100, 100, 100, 100, 100, 100, 100]), "NO")
test.assert_equals(tickets([25, 25, 25, 25, 50, 100, 50]), "YES")
test.assert_equals(tickets([50, 100,100]), "NO")
test.assert_equals(tickets([25, 25, 100]), "NO")
test.assert_equals(tickets([25, 25, 25, 25, 25, 25, 25, 50, 50, 50, 100, 100, 100, 100]), "NO")
test.assert_equals(tickets([25, 25, 50, 50, 100]), "NO")
test.assert_equals(tickets([25, 50, 50]), "NO")
test.assert_equals(tickets([25, 25, 25, 100]), "YES")
test.assert_equals(tickets([25, 50, 25, 100]), "YES")
test.assert_equals(tickets([25, 25, 25, 25, 25, 100, 100]), "NO")