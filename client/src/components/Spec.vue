<template>
  <div class="box">

  <div id ="spec">

      <h1 style= "font-family:futura;"> {{title}}</h1>

      <hr size = "1" align="center" color="#1F6891">

      <p> {{sub1}} </p>

      <p1>  {{desc}} </p1><br>
        <p1> {{desc2}} </p1>


          <p>{{sub2}} </p>

          <p1 style = "font-style:underline;">  {{slides}}
           </p1><br><br>


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
        title: 'PROJECT TITLE',
        sub1: 'subtitle1',
        desc: "deadline 1, 2018",
        desc2: "deadline 2, 2019",
        sub2: 'subtitle2',
        slides: "docs.google.com/presentation/d/1UpyU5qLMTIgDtMDBkq9CGz9JT-MZ4gQVW8FJmqpywI4/edit?usp=sharing",
        about: "ABOUT THE PROJECT",
        info: `This is a lot of dummy text about the project that is being described in this spec, soldering, breadboards, schematic, IEEE lab, OPS
         In this project, you will be making an LED light up! The first step will be to create the circuit from the schematic on your breadboard. Do this by using your knowledge of breadboards, and bending your component leads 90 degrees and sticking them in the breadboard. After you've done that, bring it to an officer to look at and they'll ask you some questions about it. Then, you'll solder your circuit to a perfboard. Keep a look out for sign up times for soldering with supervision! In summary, this project entails: `

    }
  }
}
</script>

<style scoped>

.box
{
  border: 1px;
  padding: 0 0 15px;
  margin: 15px 15px;
 -webkit-box-shadow: 2px 3px 8px #eee;
-moz-box-shadow: 2px 3px 8px #eee;
box-shadow: 0 0 12px 5px #d3d3d3;
padding: 50px;
}


h1 {
  text-align: center;
  color: #1F6891;
  font-weight:normal;
}

p
{
  font: 16px Futura;
  color: #1F6891;
}


p1
{
  font: 12px Futura;
  color: black;
}


hr
{
  color: #1F6891;
}

</style>
