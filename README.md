# HasuraFlipBookChallenge
Design a language for describing flipbooks and implement a compiler for this language that can convert a flipbook description into a printable PDF(or video).

# How to run:
Place the input flip file inside input folder and output files can be seen at output folder  <br />
for generating video: <br />
**main.py human_life_span.flip -o human_life_span.mp4 </br>**

for generating pdf: <br />
**main.py human_life_span.flip -o human_life_span.pdf </br>**

# Sample Input: input/human_life_span.flip
frames (1,5) age1.png <br />
frames (6,10) age2.png <br />
frames(11,15) age3.png <br />
frames (16,20) age4.png <br />
frames (21,25) age5.png <br />
frames(26,30) age6.png <br />
frames (31,35) age7.png <br />
frames (36,40) age8.png <br />
frames(41,45) age9.png <br />
frames (46,50) age10.png <br />

# Sample Output:
 output folder contains both pdf and mp4 files of human_life_span.flip input file
 
# Further enhancements:
 Primitives required for showing apple falling on Newton's head
 We can add further enhancements like <br/>
 position for initial positioning coordinates of image from top-left  (Created position class in Tokens folder)</br> 
 scaling for increasing the dimensions(height, width) of image   </br>
 move for movement the image by x user units on x-axis, y user units on y-axis on every page </br>
