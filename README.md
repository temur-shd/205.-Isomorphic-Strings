# 205.-Isomorphic-Strings
205. İzomorfik Dizeler

S ve t izmorfik olup olmadığını ölçmek istediğimiz iki dizedir.
İzomorfiklik izelerdeki karaklerlerin birbirrine map olması (eşleşmesi) demektir.
Ancak hiçbir iki karakter aynı karaktere eşlenemez, ancak bir karakter kendi kendine eşlenebilir.


Kısıtlamalar:
1 <= s.length <= 5 * 104
t.length == s.length
s ve t herhangi bir geçerli ascıı karakterinden oluşur.

Example:
Input: s = "egg", t = "add"
Output: true

e-->g ile eşleşmiş, g-->d ile eşleşmiş ikinci g ye de d harfi geldiği için doğru diyoruz.

Input: s = "foo", t = "bar"
Output: false

f-->b ile eşleşmiş, o-->a ile eşleşmiş ancak 2. o-->r gelmiş yanlış.

**HashMap kullanarak çözülebilir. Böylece karmaşıklık O(n) olur.**
Eşleşmeler için mapST ve mapTS olacak şekilde tanımlama yaparak c1 ve c2'ye sırasıyla s ve t dizesini atadık 
Daha sonra hız kazanmak adına for döngüsü yerine zip() fonksiyonu kullanılır (Aldığı iki parametrenin liste tipinde olduğunu farz edersek, iki parametreyi alır ve ikili demet yapısında yeni bir liste oluşturur.)
