
for(var i=0; i<a_name.length ; i++){
 //href 
 var name = a_name[i];
 var id = name.split(" ").join(""); 


 // should be in percentage -> width: 25%
 var progress_bar_person = progress_bar[a_name[i]];

 // Summary
 var personality_text = summary[a_name[i]];

 //Big 4 trais person
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

 //main div tag
 var main = document.createElement('div');
 
 main.setAttribute("id", id);
 main.setAttribute("role", "tabpanel");
 if (i==0) {
    main.setAttribute("aria-expanded", "true");
    main.setAttribute("class","tab-pane active");
  }
else{
    main.setAttribute("aria-expanded", "false");
    main.setAttribute("class","tab-pane");
}
 //main.setAttribute("aria-expanded", "true");

 //row tag 
 var row_1 = document.createElement('div');
 row_1.classList.add("row");

 //column 1 tag
 var col_1 = document.createElement('div');
 col_1.setAttribute("class", "col-md-4 ml-auto mr-auto");


 //Anxiety
 //text 1 div left
 var bar_1 = document.createElement('div');
 bar_1.classList.add("text-left");

 //paragraph 1
 var p_1 = document.createElement('p');
 p_1.textContent = "Anxiety";

 //progress 1
 var progress_1 = document.createElement('div');
 progress_1.classList.add("progress");

 //progress attribute 1 
 var attribute_1 = document.createElement('div');
 attribute_1.setAttribute("class","progress-bar bg-success");
 attribute_1.setAttribute("role", "progressbar");
 attribute_1.setAttribute("style", progress_bar_person[0]);
 attribute_1.setAttribute("aria-valuenow", "25");
 attribute_1.setAttribute("aria-valuemin", "0");
 attribute_1.setAttribute("aria-valuemax", "100");

 //break_1
 var br_1 = document.createElement('br');

 //Appending child Attribute 1
 progress_1.appendChild(attribute_1);
 bar_1.appendChild(p_1);
 bar_1.appendChild(progress_1);
 bar_1.appendChild(br_1);
 col_1.appendChild(bar_1);

 //Friendliness
 //text 2 div 
 var bar_2 = document.createElement('div');
 bar_2.classList.add("text-left");

 //paragraph 2
 var p_2 = document.createElement('p');
 p_2.textContent = "Friendliness";

 //progress 2
 var progress_2 = document.createElement('div');
 progress_2.classList.add("progress");

 //progress attribute 2 
 var attribute_2 = document.createElement('div');
 attribute_2.setAttribute("class","progress-bar bg-warning");
 attribute_2.setAttribute("role", "progressbar");
 attribute_2.setAttribute("style", progress_bar_person[1]);
 attribute_2.setAttribute("aria-valuenow", "25");
 attribute_2.setAttribute("aria-valuemin", "0");
 attribute_2.setAttribute("aria-valuemax", "100");

 //break_2
 var br_2 = document.createElement('br');

 //Appending child Attribute 2
 progress_2.appendChild(attribute_2);
 bar_2.appendChild(p_2);
 bar_2.appendChild(progress_2);
 bar_2.appendChild(br_2);
 col_1.appendChild(bar_2);

 //Morality
 //text 3 div 
 var bar_3 = document.createElement('div');
 bar_3.classList.add("text-left");

 //paragraph 3
 var p_3 = document.createElement('p');
 p_3.textContent = "Morality";

 //progress 3
 var progress_3 = document.createElement('div');
 progress_3.classList.add("progress");

 //progress attribute 3 
 var attribute_3 = document.createElement('div');
 attribute_3.setAttribute("class","progress-bar bg-info");
 attribute_3.setAttribute("role", "progressbar");
 attribute_3.setAttribute("style", progress_bar_person[2]);
 attribute_3.setAttribute("aria-valuenow", "25");
 attribute_3.setAttribute("aria-valuemin", "0");
 attribute_3.setAttribute("aria-valuemax", "100");

 //break_3
 var br_3 = document.createElement('br');

 //Appending child Attribute 3
 progress_3.appendChild(attribute_3);
 bar_3.appendChild(p_3);
 bar_3.appendChild(progress_3);
 bar_3.appendChild(br_3);
 col_1.appendChild(bar_3);

 //Introversion/Extraversion
 //text 4 div 
 var bar_4 = document.createElement('div');
 bar_4.classList.add("text-left");

 //paragraph 4
 var p_4 = document.createElement('p');
 p_4.textContent = "Introversion/Extraversion";

 //progress 4
 var progress_4 = document.createElement('div');
 progress_4.classList.add("progress");

 //progress attribute 4 
 var attribute_4 = document.createElement('div');
 attribute_4.setAttribute("class","progress-bar bg-danger");
 attribute_4.setAttribute("role", "progressbar");
 attribute_4.setAttribute("style", progress_bar_person[3]);
 attribute_4.setAttribute("aria-valuenow", "25");
 attribute_4.setAttribute("aria-valuemin", "0");
 attribute_4.setAttribute("aria-valuemax", "100");

 //break_4
 var br_4 = document.createElement('br');

 //Appending child Attribute 4
 progress_4.appendChild(attribute_4);
 bar_4.appendChild(p_4);
 bar_4.appendChild(progress_4);
 bar_4.appendChild(br_4);
 col_1.appendChild(bar_4);

     //Trust
 //text 5 div 
 var bar_5 = document.createElement('div');
 bar_5.classList.add("text-left");

 //paragraph 5
 var p_5 = document.createElement('p');
 p_5.textContent = "Trust";

 //progress 5
 var progress_5 = document.createElement('div');
 progress_5.classList.add("progress");

 //progress attribute 5 
 var attribute_5 = document.createElement('div');
 attribute_5.setAttribute("class","progress-bar");
 attribute_5.setAttribute("role", "progressbar");
 attribute_5.setAttribute("style", progress_bar_person[2]);
 attribute_5.setAttribute("aria-valuenow", "25");
 attribute_5.setAttribute("aria-valuemin", "0");
 attribute_5.setAttribute("aria-valuemax", "100");

 //break_5
 var br_5 = document.createElement('br');

 //Appending child Attribute 5
 progress_5.appendChild(attribute_5);
 bar_5.appendChild(p_5);
 bar_5.appendChild(progress_5);
 bar_5.appendChild(br_5);
 col_1.appendChild(bar_5);


 //column 2 tag
 var col_2 = document.createElement('div');
 col_2.setAttribute("class", "col-md-6 ml-auto mr-auto");


 //summary card 
 var card_sum = document.createElement('div');
 card_sum.setAttribute("class", "card bg-light");

 //card header 
 var card_header = document.createElement('div');
 card_header.setAttribute("class", "card-header");
 card_header.textContent = "Personality Glimps";

//card body
var card_body = document.createElement('div');
card_body.setAttribute("class", "card-body");

//card title
var  card_title = document.createElement('h5');
card_title.setAttribute("class", "card-title");
card_title.textContent = name;

//summary 
var text_summary = document.createElement('p');
text_summary.setAttribute("class", "card-text");
text_summary.textContent = personality_text;

//compile
card_sum.appendChild(card_header);
card_body.appendChild(card_title);
card_body.appendChild(text_summary);
card_sum.appendChild(card_body);
col_2.appendChild(card_sum);

// Add the two col to the row
row_1.appendChild(col_1);
row_1.appendChild(col_2);



// Append to main 
main.appendChild(row_1);


//Adding it to the parent div
var tab_content  = document.getElementById("my-tab-content");
tab_content.appendChild(main);
}