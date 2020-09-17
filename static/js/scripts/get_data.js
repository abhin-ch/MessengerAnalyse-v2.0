
function get_data(json){
    
    // replace first and last characters with whitespace
    json = json.replace('\"', "");
    json = json.replace(/.$/,"");
    json = JSON.parse(json);

    data = {}; // Save parsed json in different object

    // Convert string to json object
    for (var n of Object.keys(json)) {
        data[n] = JSON.parse(json[n]);
    }
    console.log(data);
    return data;
}

