import sys; sys.stdin = open("26766.txt", "r")

N = int(input())
heart = ''' @@@   @@@ 
@   @ @   @
@    @    @
@         @
 @       @ 
  @     @  
   @   @   
    @ @    
     @     '''
for i in range(N):
    print(heart)