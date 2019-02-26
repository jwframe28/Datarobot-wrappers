def batch_predictions(project_id,df_path):
    

    project = dr.Project.get(project_id)

    models = project.get_models()
    model_final = models[0]
    model_id = model_final.id

    model = dr.Model.get(project=project_id,
                      model_id=model_id)

    dataset_from_path = project.upload_dataset(df_path)


    predict_job = model.request_predictions(dataset_from_path.id)

    print('fetching results')
    predictions = predict_job.get_result_when_complete()

    
    return predictions
