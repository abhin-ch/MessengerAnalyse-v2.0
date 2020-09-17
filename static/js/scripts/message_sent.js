// Getting Data 
var message_count = data['message_count_percent'];
var a_name = Object.keys(message_count);
var a_data = Object.values(message_count) ;
var ctx = document.getElementById("message_sent").getContext('2d');
ctx.shadowBlur = 200;
ctx.shadowColor = "black";
console.log("The Graph is working ")
var chart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: a_name,
        datasets: [{
        label: "Message Sent",
        backgroundColor: list_name_colour,
        data: a_data
        }]
    },
    options: {}
});