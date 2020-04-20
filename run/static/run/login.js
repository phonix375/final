window.addEventListener('DOMContentLoaded', (event) => {
     var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            label: 'My First dataset',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: [0, 10, 5, 2, 20, 30, 45]
        }]
    },

    // Configuration options go here
    options: {}
});


     let register = document.querySelector("#register");
     register.addEventListener('click', function(){
          document.querySelector('#loginForm').style.display = 'none';
          document.querySelector('#loginText').style.display = 'none';
          document.querySelector('#registerForm').style.display= 'flex';
          document.querySelector('#registerText').style.display = 'flex';
     });
     let loginbtn = document.querySelector('#loginbtn');
     loginbtn.addEventListener('click', function(){
          document.querySelector('#loginForm').style.display = 'flex';
          document.querySelector('#loginText').style.display = 'flex';
          document.querySelector('#registerForm').style.display= 'none';
          document.querySelector('#registerText').style.display = 'none';
     });
 });