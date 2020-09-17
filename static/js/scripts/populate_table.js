var word_count = data['word_count'];
var msg_count = data['message_count'];
var a_name = Object.keys(word_count);
console.log("This variable is comming from populate_table.js");
console.log(a_name);
var a_word = Object.values(word_count);
var a_msg = Object.values(msg_count);
//Read the file from the URL
        for(var i=0; i<a_name.length ; i++){
        console.log("Hey I am abby ")
        var $tr = $("<tr>");
        var $name = $("<td>");
        var $message = $("<td>");
        var $wordsent = $("<td>");
        var $avgword = $("<td>");
        $name.append(a_name[i]);
        $message.append(a_word[i]);
        $wordsent.append(a_msg[i]);
        var avgwor = a_word[i]/a_msg[i];
        $avgword.append(avgwor.toFixed(1));
        $tr.append($name);
        $tr.append($wordsent);
        $tr.append($message);
        $tr.append($avgword);
        $('#summary').append($tr);
        }


function num_string(d){
        var perce = d*100;
        var sign = "%";
        var ret = perce+sign;
        return ret;
}