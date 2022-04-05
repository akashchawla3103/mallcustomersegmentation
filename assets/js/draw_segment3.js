var data = [{
    values: [male[2], female[2]],
    labels: ['males', 'females'],
    type: 'pie',
    marker: {
        colors: ultimateColors[0]
    }
}];
var layout = {
    height: 400,
    width: 500
};
var layout = {
    title: 'Male to Female Distribution'
}
var config = {
    responsive: true
}
Plotly.newPlot('drawsegment_3', data, layout, config);
//
var data = [{
    x: ['21+', '21-'],
    y: [plus[2], minus[2]],
    type: 'bar',

    marker: {
        color: 'rgb(82, 30, 105)',
    }

}];
var layout = {
    title: 'Age Distribution'
}
config = {
    responsive: true
}

Plotly.newPlot('drawsegment_3.1', data, layout, config);