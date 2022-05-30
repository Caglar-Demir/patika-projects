# Insertion Sort
## [22,27,16,2,18,6] -> Insertion Sort

## Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.
  - [2,27,16,22,18,6]
  - [2,6,16,22,18,27]
  - [2,6,16,18,22,27]
## Big-O gösterimini yazınız.
  - n + (n-1) + (n-2) + ... + 1 = n * (n+1) / 2 --> O(n^2)
## Time Complexity: 
  ### Average case: Aradığımız sayının ortada olması
    - O(n^2)
  ### Worst case: Aradığımız sayının sonda olması
    - O(n^2)
  ### Best case: Aradığımız sayının dizinin en başında olması.
    - O(n)
## Dizi sıralandıktan sonra 18 sayısı hangi case kapsamına girer? Yazınız.
  - 18 dizinin en küçük değeri olsa O(1) olarak best case, en büyük değer olsa O(n) olarak worst case olurdu.
  - Bu iki durumda olmadığı için 18 sayısı average case olacaktır.

## [7,3,5,8,2,9,4,15,6] dizisinin Insertion Sort'a göre ilk 4 adımını yazınız.
  - [2,3,5,8,7,9,4,15,6]
  - [2,3,4,8,7,9,5,15,6]
  - [2,3,4,5,7,9,8,15,6]
  - [2,3,4,5,6,9,8,15,7]