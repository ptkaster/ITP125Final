Paul Kaster
5318323379
ITP 125 McGregor TTh 6-9pm

Instructions to run:
  Make sure python 2 is installed
  Run with command:
  python finalProject125.py



Passwords and crack times:
  Z - 0.0001380443573 seconds
  AD - 0.00558495521545 seconds
  God - 0.317130088806 seconds
  1234 - 26.6604969501 seconds
  AbCdE - 1,157.25627899 seconds
  Trojan - 61,302.462079 seconds
  F1ghtOn - 3,249,030.49019 seconds (estimated, not cracked)
  P@ssword - 172,198,615.98 seconds (estimated, not cracked)



Analysis:
  The algorithm runs in Θ(53^n) where n is the password length. Of course this
  means that longer passwords take longer to crack, but it also means that you
  can estimate time to crack based off of password length. When you look at the
  passwords you gave us, you see that an increase in password length of one
  character leads to on average a 55x increase in time to crack (theory says this
  should be 53x but there is always some variance).

  I could have made the cracking go faster by a couple of methods. One would be
  to implement multiprocessing, which would theoretically improve performance by
  up to 4x on my four cores. Another would be to use pre-computed tables which
  can be searched in Θ(log(53^n)) which would be a massive runtime improvement
  but could be more costly in space complexity.



Appendix notes:

  Tested compilation environment:
    Python 2.7.10 (default, Feb 22 2019, 21:17:52)
    [GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.37.14)] on darwin

  Dependencies:
    hashlib (I believe it's a standard library though)

  Source for hashing library: https://github.com/python/cpython/blob/3.7/Lib/hashlib.py
  List of password special characters: https://www.owasp.org/index.php/Password_special_characters
