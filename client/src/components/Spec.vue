<template>
  <div class="box">

  <div id ="spec">

      <h1 style= "font-family:futura;"> {{title}}</h1>

      <hr size = "1" align="center" color="#1F6891">

      <p align="left"> {{sub1}} </p>

<div class= "left">
      <p1> {{desc}} <br> {{desc2}} </p1>
    </div>

<br><br>
          <p align="left">{{sub2}} </p>

<div class= "left">
          <p1 style = "font-style:underline;">  {{slides}}
           </p1>
         </div><br><br>


           <p align ="center"> {{about}} </p>

            <hr size = "1" align="center" color="#1F6891">

            <p1> {{info}}</p1>



  </div>
</div>
</template>




<script>
export default {
  name: 'spec',
  data() {
    return {
        title: 'LED BLINKER',
        sub1: 'DEADLINES:',
        desc: "deadline 1, 2018",
        desc2: "deadline 2, 2019",
        sub2: 'SLIDES:',
        slides: "docs.google.com/presentation/d/1UpyU5qLMTIgDtMDBkq9CGz9JT-MZ4gQVW8FJmqpywI4/edit?usp=sharing",
        about: "ABOUT THE PROJECT",
        info: `Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus euismod mi et porta sagittis. Fusce rutrum orci sed iaculis porta. Suspendisse egestas eleifend nunc non lobortis. Quisque orci sapien, sagittis elementum mollis dapibus, vestibulum vel arcu. Mauris quis ex ac urna scelerisque cursus quis at tortor. Duis dignissim faucibus magna vel mollis. Vestibulum at vehicula lorem, quis tempus mi. In eget enim magna. Proin ultrices congue quam, bibendum malesuada metus cursus at. Vivamus feugiat nibh sed lorem faucibus efficitur. Sed a est at purus ullamcorper dignissim.

Nullam est libero, consequat quis metus ut, convallis volutpat risus. Sed vitae sagittis nunc, vel ultrices nisl. Vestibulum vitae lacinia augue. Duis vitae libero mauris. Duis rutrum sit amet nisl tincidunt maximus. Vivamus tristique justo at arcu lacinia, ac varius turpis sollicitudin. Morbi eu velit rutrum, venenatis neque a, vehicula risus. Nullam posuere dictum dolor quis pellentesque. Praesent fringilla commodo malesuada. Nam scelerisque, massa sed elementum malesuada, libero diam varius lacus, in aliquam tortor lorem ut metus. Aliquam luctus felis facilisis tellus faucibus suscipit. Praesent metus diam, accumsan eget dolor non, facilisis cursus libero. Donec venenatis dolor sed mollis tempor.

In mattis tempor sollicitudin. Donec vitae faucibus quam, ultrices euismod mi. Aliquam molestie, odio sed fermentum tempus, arcu risus efficitur nisl, vel gravida massa erat vitae diam. Integer ut leo augue. Morbi tristique interdum convallis. Curabitur in ornare diam. Aliquam eleifend nunc vitae ante blandit maximus.

Proin vel nisi sit amet diam interdum dapibus quis a dolor. Morbi dignissim blandit erat, ut vehicula leo vestibulum sit amet. Sed ante risus, fermentum quis rutrum sit amet, lacinia a est. Praesent non felis quis enim bibendum semper. Integer luctus gravida dui a vulputate. In dictum scelerisque varius. Donec tempus tempor bibendum. In quis lectus hendrerit, sodales magna eget, facilisis diam. Etiam et aliquet nulla. Quisque at est sit amet nisi ultricies molestie vel sed quam. Suspendisse potenti.

Etiam bibendum eu dui ac suscipit. Nunc non ante justo. Praesent aliquet ullamcorper viverra. Pellentesque eleifend nisi placerat vulputate maximus. Integer aliquam fringilla nibh vel varius. Pellentesque ac tristique risus, a rutrum lectus. Aenean pretium enim et faucibus auctor. Maecenas sit amet suscipit purus. Morbi in mauris finibus, sollicitudin odio sed, pulvinar ex. Aliquam at nisi non justo dignissim semper. Donec vehicula enim scelerisque ante blandit, ut accumsan purus suscipit. Vestibulum rutrum faucibus ex, quis vehicula orci laoreet id.`
    }
  }
}
</script>

<style scoped>

.box
{
margin-top: 65px;
margin-left: auto;
margin-right: auto;
width: 50%;
height: 100%;
padding-top: 25px;
padding-left: 50px;
padding-right: 50px;
padding-bottom: 25px;

background: #FFFFFF;
box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.2);
overflow: hidden;
}


h1 {

  font-family: Futura;
  font-style: normal;
  font-weight: 500;
  font-size: 24px;
  line-height: 32px;

  color: #1F6891;
}

p
{
  font-family: Futura;
  font-style: normal;
  font-weight: 500;
  font-size: 14px;
  line-height: 19px;
  /* identical to box height */

  color: #1F6891;
}


p1
{
  font-family: Futura;
  font-style: normal;
  font-weight: 500;
  font-size: 12px;
  line-height: 16px;
  width: 100%;
  text-align: left;

  color: #000000;
}


hr
{
  color: #1F6891;
left: 10.7%;
right: 31.56%;
top: 22.56%;
bottom: 77.44%;
}

.left{
    float: left;
}

</style>
