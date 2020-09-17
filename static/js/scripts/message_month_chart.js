console.log(data);
var msg_by_time = data['message_by_month_group'];
var d_name = Object.keys(msg_by_time);
var d_data = Object.values(msg_by_time);
var ctx = document.getElementById('month').getContext('2d');
var lab3 = [];
for (var i = 0; i < d_name.length; i++) {
    dict = {label:d_name[i], backgroundColor: list_name_colour[i], data:d_data[i]};
    lab3.push(dict);
}
console.log("Hey Please Look Here");
console.log(lab3);
var chart = new Chart(ctx, {
    // The type of chart 
    type: 'bar',
    // The data for the dataset
    data: {
      labels: ["Jan","Feb","Mar","Apr","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
      datasets: lab3
    },
    options: {scales: {xAxes: [{gridLines: {drawOnChartArea: false,  color: 'transparent'},barPercentage: 0.6 }],
                yAxes: [{gridLines: {drawOnChartArea: false}, display:false}]}}
});
