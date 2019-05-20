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
        info: `This is a lot of dummy text about the project that is being described in this spec, soldering, breadboards, schematic, IEEE lab, OPS
         In this project, you will be making an LED light up! The first step will be to create the circuit from the schematic on your breadboard. Do this by using your knowledge of breadboards, and bending your component leads 90 degrees and sticking them in the breadboard. After you've done that, bring it to an officer to look at and they'll ask you some questions about it. Then, you'll solder your circuit to a perfboard. Keep a look out for sign up times for soldering with supervision! In summary, this project entails:  adding more to see how the box responds to browser  adding more to see how the box responds to browser  adding more to see how the box responds to browser  adding more to see how the box responds to browser  adding more to see how the box responds to browser  adding more to see how the box responds to browser  adding more to see how the box responds to browser  adding more to see how the box adding more to see how the box responds to browser  adding more to see how the box responds to browser  adding more to see how the box responds to browser  adding more to see how the box responds to browser  adding more to see how the box responds to browser  adding more to see how the box responds to browser  adding more to see how the box responds to browser  adding more to see how the box responds to browser  adding more to see how the box responds to browser  responds to browser `

    }
  }
}
</script>

<style scoped>

.box
{
margin-top: 65px;
margin-left: 85px;
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
