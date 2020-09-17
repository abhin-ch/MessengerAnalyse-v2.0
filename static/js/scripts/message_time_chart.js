var msg_by_time = data['message_by_hour_group'];
var d_name = Object.keys(msg_by_time);
var d_data = Object.values(msg_by_time);
var ctx = document.getElementById('time').getContext('2d');
var lab3 = [];
for (var i = 0; i < d_name.length; i++) {
    dict = {label:d_name[i], backgroundColor: list_name_colour[i], borderColor: list_name_colour[i] ,data:d_data[i]};
    lab3.push(dict);
}
console.log("Hey Please Look Here");
console.log(lab3);
var chart = new Chart(ctx, {
    // The type of chart 
    type: 'line',
    // The data for the dataset
    data: {
      labels: ["0", "1","2","3","4","5","6","7","8","9","10","11","12","13", "14","15","16","17","18","19","20","21","22","23"],
      datasets: lab3
    },
    options: { bezierCurve : false, scales: {xAxes: [{gridLines: {drawOnChartArea: false,  color: 'transparent'},barPercentage: 0.6}],
    yAxes: [{gridLines: {drawOnChartArea: false}, display:false}]}}
});