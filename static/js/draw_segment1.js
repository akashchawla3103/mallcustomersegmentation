var data = [{
    values: [male[0], female[0]],
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

Plotly.newPlot('drawsegment_1', data, layout, config);

var data = [{
    x: ['21+', '21-'],
    y: [plus[0], minus[0]],
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

Plotly.newPlot('drawsegment_1.1', data, layout, config);