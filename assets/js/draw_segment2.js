var data = [{
    values: [male[1], female[1]],
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
Plotly.newPlot('drawsegment_2', data, layout, config);
//
var data = [{
    x: ['21+', '21-'],
    y: [plus[1], minus[1]],
    type: 'bar',

    marker: {
        color: 'rgb(82, 30, 105)',
    }

}];
var layout = {
    title: 'Age Distribution'
}
var config = {
    responsive: true
}

Plotly.newPlot('drawsegment_2.1', data, layout, config);