# shirLink
**
DESCRIPTION
**
Simple URL shortner using Django. This version generate unique IDs on client and server side as an example - Shorter Urls are created using Server Generated UID. Client Generate ID creates URL in DB, but those are not exposed to the user.

Function to Generate UID o client side - ID Composed by 5 alpha-numeric characters.

      function generateUID() {
          // I generate the UID from two parts here 
          // to ensure the random number provide enough bits.
          var firstPart = (Math.random() * 46656) | 0;
          var secondPart = (Math.random() * 46656) | 0;
          firstPart = ("000" + firstPart.toString(36)).slice(-3);
          secondPart = ("000" + secondPart.toString(36)).slice(-3);
          return firstPart + secondPart;
      }
