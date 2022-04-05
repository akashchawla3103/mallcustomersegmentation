var data = [{
    values: [male[4], female[4]],
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
Plotly.newPlot('drawsegment_5', data, layout, config);
//
var data = [{
    x: ['21+', '21-'],
    y: [plus[4], minus[4]],
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
Plotly.newPlot('drawsegment_5.1', data, layout, config);