module MetricRegLearn

export metric_score  

function metric_score(r2::Float64, mape::Float64)
    final_score = ((1 - mape) + r2) / 2 * 100
    return final_score
end

end 