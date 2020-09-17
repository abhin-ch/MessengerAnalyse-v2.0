
for(var i=0; i<a_name.length ; i++){
    //href 
    var name = a_name[i];
    var id = name.split(" ").join(""); 
    var big_four_person =  big_four[a_name[i]];
    // Canvas Id -> chart1AbhinavChaudhary
   var rs1 = "chart1";
   var rs2 = "chart2";
   var rs3 = "chart3";
   var rs4 = "chart4";
    var donout_1 = rs1.concat(id);
    var donout_2 = rs2.concat(id);
    var donout_3 = rs3.concat(id);
    var donout_4 = rs4.concat(id);
    agreeableness(donout_1, big_four_person[0]);
    consci(donout_2, big_four_person[1]);
    openness(donout_3, big_four_person[2]);
    emotional(donout_4, big_four_person[3]);
}