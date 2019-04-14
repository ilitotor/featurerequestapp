'''
To do the test I used https://colab.research.google.com/

!pip install -q fernet
!pip install -q cryptography 

'''
from cryptography.fernet import Fernet

Key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABcrNNu4qnVosimaa5S1h5cMM-EteJtXNkQ0YnyXJSq08Hj9m6tTfWbMoSNc7IUPXqNIh_wLYS_rqa8jABOOcb7n1ydFte6jtPZb4tKlBkIxJNoNFXKKQH1wJqbHtV-9pl8t2AidqKO4tefdqivNuL9gOg_pdkT4Z9eqsOLgKWtu2vuqRbnDxDxZTQ9V1x5piwhaC-6'

f = Fernet(Key)
print(f.decrypt(message))
