// Big Four Chart 
var row_2 = document.createElement('div');
row_2.setAttribute("class","row");

// col 1 for row 2
var col_12 = document.createElement('div');
col_12.setAttribute("class", "col-md-3");

// donout card 1
var donout_card_1 = document.createElement('div');
donout_card_1.setAttribute("class", "card");

// donout header card 1
var donout_header_1 = document.createElement('div');
donout_header_1.setAttribute("class", "card-header");

// donout tittle card 1
var donout_title_1 = document.createElement('h5');
donout_title_1.setAttribute("class", "card-title");
donout_title_1.textContent = "Agreeableness";

// donout paragragh card 1
var donout_paragraph_1 = document.createElement('p');
donout_paragraph_1.setAttribute("class", "card-category");

// compiling header 1 
donout_header_1.appendChild(donout_title_1);
donout_header_1.appendChild(donout_paragraph_1);
donout_card_1.appendChild(donout_header_1);


// donout body card 1
var donout_body_1 = document.createElement('div');
donout_body_1.setAttribute("class", "card-body");

//canvas 1 
var canvas_1 = document.createElement('canvas');
canvas_1.setAttribute("id", donout_1);
canvas_1.setAttribute("class", "ct-chart ct-perfect-fourth");
canvas_1.setAttribute("width", "456");
canvas_1.setAttribute("height", "300");

//compiling body 1
donout_body_1.appendChild(canvas_1);

//script for canvas 1


var chart = "chartDonut1";
console.log(donout_1);
//card 1 Footer
var donout_footer_1 = document.createElement('div');
donout_footer_1.setAttribute("class", "card-footer");

// footer legend 1 
var donout_legend_1 = document.createElement('div');
donout_legend_1.setAttribute("id", "legend1");
donout_legend_1.setAttribute("class", "lengend");
donout_legend_1.textContent = " Score";

// footer icon 1 
var donout_icon_1 = document.createElement('i');
donout_icon_1.setAttribute("class", "fa fa-circle text-primary");

// hr 1
var donout_hr = document.createElement('hr');

//footer stat 1
var donout_stat_1 = document.createElement('div');
donout_stat_1.setAttribute("class", "stats");
donout_stat_1.textContent = "Updated Just Now";

// footer calender icon 1 
var donout_icon_callender_1 = document.createElement('i');
donout_icon_callender_1.setAttribute("class", "fa fa-history")

//compiling the footer 1
donout_footer_1.appendChild(donout_legend_1);
donout_footer_1.appendChild(donout_icon_1);
donout_footer_1.appendChild(donout_hr);
donout_footer_1.appendChild(donout_stat_1);
donout_footer_1.appendChild(donout_icon_callender_1);

// complilin the header body and fotter 1
donout_card_1.appendChild(donout_header_1);
donout_card_1.appendChild(donout_body_1);
donout_card_1.appendChild(donout_footer_1);
col_12.appendChild(donout_card_1);







// col 2 for row 2
var col_22 = document.createElement('div');
col_22.setAttribute("class", "col-md-3");

// donout card 2
var donout_card_2 = document.createElement('div');
donout_card_2.setAttribute("class", "card");

// donout header card 2
var donout_header_2 = document.createElement('div');
donout_header_2.setAttribute("class", "card-header");

// donout tittle card 2
var donout_title_2 = document.createElement('h5');
donout_title_2.setAttribute("class", "card-title");
donout_title_2.textContent = "Conscientiousness";

// donout paragragh card 2
var donout_paragraph_2 = document.createElement('p');
donout_paragraph_2.setAttribute("class", "card-category");

// compiling header 2 
donout_header_2.appendChild(donout_title_2);
donout_header_2.appendChild(donout_paragraph_2);
donout_card_2.appendChild(donout_header_2);


// donout body card 2
var donout_body_2 = document.createElement('div');
donout_body_2.setAttribute("class", "card-body");

//canvas 2 
var canvas_2 = document.createElement('canvas');
canvas_2.setAttribute("id", donout_2);
canvas_2.setAttribute("class", "ct-chart ct-perfect-fourth");
canvas_2.setAttribute("width", "456");
canvas_2.setAttribute("height", "300");

//compiling body 2
donout_body_2.appendChild(canvas_2);

//card 2 Footer
var donout_footer_2 = document.createElement('div');
donout_footer_2.setAttribute("class", "card-footer");

// footer legend 2 
var donout_legend_2 = document.createElement('div');
donout_legend_2.setAttribute("id", "legend2");
donout_legend_2.setAttribute("class", "lengend");
donout_legend_2.textContent = " Score";

// footer icon 2 
var donout_icon_2 = document.createElement('i');
donout_icon_2.setAttribute("class", "fa fa-circle text-primary");

// hr 2
var donout_hr = document.createElement('hr');

//footer stat 2
var donout_stat_2 = document.createElement('div');
donout_stat_2.setAttribute("class", "stats");
donout_stat_2.textContent = "Updated Just Now";

// footer calender icon 2
var donout_icon_callender_2 = document.createElement('i');
donout_icon_callender_2.setAttribute("class", "fa fa-history")

//compiling the footer 2
donout_footer_2.appendChild(donout_legend_2);
donout_footer_2.appendChild(donout_icon_2);
donout_footer_2.appendChild(donout_hr);
donout_footer_2.appendChild(donout_stat_2);
donout_footer_2.appendChild(donout_icon_callender_2);

// complilin the header body and fotter 2
donout_card_2.appendChild(donout_header_2);
donout_card_2.appendChild(donout_body_2);
donout_card_2.appendChild(donout_footer_2);
col_22.appendChild(donout_card_2);









// col 3 for row 2
var col_32 = document.createElement('div');
col_32.setAttribute("class", "col-md-3");

// donout card 3
var donout_card_3 = document.createElement('div');
donout_card_3.setAttribute("class", "card");

// donout header card 3
var donout_header_3 = document.createElement('div');
donout_header_3.setAttribute("class", "card-header");

// donout tittle card 3
var donout_title_3 = document.createElement('h5');
donout_title_3.setAttribute("class", "card-title");
donout_title_3.textContent = "Openness";

// donout paragragh card 3
var donout_paragraph_3 = document.createElement('p');
donout_paragraph_3.setAttribute("class", "card-category");

// compiling header 3 
donout_header_3.appendChild(donout_title_3);
donout_header_3.appendChild(donout_paragraph_3);
donout_card_3.appendChild(donout_header_3);


// donout body card 3
var donout_body_3 = document.createElement('div');
donout_body_3.setAttribute("class", "card-body");

//canvas 3 
var canvas_3 = document.createElement('canvas');
canvas_3.setAttribute("id", donout_3);
canvas_3.setAttribute("class", "ct-chart ct-perfect-fourth");
canvas_3.setAttribute("width", "456");
canvas_3.setAttribute("height", "300");

//compiling body 3
donout_body_3.appendChild(canvas_3);

//card 3 Footer
var donout_footer_3 = document.createElement('div');
donout_footer_3.setAttribute("class", "card-footer");

// footer legend 3 
var donout_legend_3 = document.createElement('div');
donout_legend_3.setAttribute("id", "legend3");
donout_legend_3.setAttribute("class", "lengend");
donout_legend_3.textContent = " Score";

// footer icon 3 
var donout_icon_3 = document.createElement('i');
donout_icon_3.setAttribute("class", "fa fa-circle text-primary");

// hr 3
var donout_hr = document.createElement('hr');

//footer stat 3
var donout_stat_3 = document.createElement('div');
donout_stat_3.setAttribute("class", "stats");
donout_stat_3.textContent = "Updated Just Now";

// footer calender icon 3
var donout_icon_callender_3 = document.createElement('i');
donout_icon_callender_3.setAttribute("class", "fa fa-history")

//compiling the footer 3
donout_footer_3.appendChild(donout_legend_3);
donout_footer_3.appendChild(donout_icon_3);
donout_footer_3.appendChild(donout_hr);
donout_footer_3.appendChild(donout_stat_3);
donout_footer_3.appendChild(donout_icon_callender_3);

// complilin the header body and fotter 3
donout_card_3.appendChild(donout_header_3);
donout_card_3.appendChild(donout_body_3);
donout_card_3.appendChild(donout_footer_3);
col_32.appendChild(donout_card_3);
















// col 4 for row 4
var col_42 = document.createElement('div');
col_42.setAttribute("class", "col-md-3");

// donout card 4
var donout_card_4 = document.createElement('div');
donout_card_4.setAttribute("class", "card");

// donout header card 4
var donout_header_4 = document.createElement('div');
donout_header_4.setAttribute("class", "card-header");

// donout tittle card 4
var donout_title_4 = document.createElement('h5');
donout_title_4.setAttribute("class", "card-title");
donout_title_4.textContent = "Emotional range";

// donout paragragh card 4
var donout_paragraph_4 = document.createElement('p');
donout_paragraph_4.setAttribute("class", "card-category");

// compiling header 4 
donout_header_4.appendChild(donout_title_4);
donout_header_4.appendChild(donout_paragraph_4);
donout_card_4.appendChild(donout_header_4);


// donout body card 4
var donout_body_4 = document.createElement('div');
donout_body_4.setAttribute("class", "card-body");

//canvas 4 
var canvas_4 = document.createElement('canvas');
canvas_4.setAttribute("id", donout_4);
canvas_4.setAttribute("class", "ct-chart ct-perfect-fourth");
canvas_4.setAttribute("width", "456");
canvas_4.setAttribute("height", "300");

//compiling body 4
donout_body_4.appendChild(canvas_4);

//card 4 Footer
var donout_footer_4 = document.createElement('div');
donout_footer_4.setAttribute("class", "card-footer");

// footer legend 4 
var donout_legend_4 = document.createElement('div');
donout_legend_4.setAttribute("id", "legend4");
donout_legend_4.setAttribute("class", "lengend");
donout_legend_4.textContent = " Score";

// footer icon 4 
var donout_icon_4 = document.createElement('i');
donout_icon_4.setAttribute("class", "fa fa-circle text-primary");

// hr 4
var donout_hr = document.createElement('hr');

//footer stat 4
var donout_stat_4 = document.createElement('div');
donout_stat_4.setAttribute("class", "stats");
donout_stat_4.textContent = "Updated Just Now";

// footer calender icon 4
var donout_icon_callender_4 = document.createElement('i');
donout_icon_callender_4.setAttribute("class", "fa fa-history")

//compiling the footer 4
donout_footer_4.appendChild(donout_legend_4);
donout_footer_4.appendChild(donout_icon_4);
donout_footer_4.appendChild(donout_hr);
donout_footer_4.appendChild(donout_stat_4);
donout_footer_4.appendChild(donout_icon_callender_4);

// complilin the header body and fotter 4
donout_card_4.appendChild(donout_header_4);
donout_card_4.appendChild(donout_body_4);
donout_card_4.appendChild(donout_footer_4);
col_42.appendChild(donout_card_4);


// Append to row
row_2.appendChild(col_12);
row_2.appendChild(col_22);
row_2.appendChild(col_32);
row_2.appendChild(col_42);
