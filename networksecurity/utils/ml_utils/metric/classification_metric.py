from networksecurity.entity.artifact_entity import ClassificationMetricArtifact
from networksecurity.exception.exception import NetworkSecurityException
from sklearn.metrics import f1_score,precision_score,recall_score
import sys

def get_classification_score(y_true,y_pred)->ClassificationMetricArtifact:
    """
    This function calculates the classification score for the given true and predicted values.
    
    Args:
        y_true (list): The true labels.
        y_pred (list): The predicted labels.
        
    Returns:
        ClassificationMetricArtifact: An object containing the classification metrics.
    """
    try:
        model_f1_score = f1_score(y_true, y_pred)
        model_precision_score = precision_score(y_true, y_pred)
        model_recall_score = recall_score(y_true, y_pred)
        
        classification_metric = ClassificationMetricArtifact(
            f1_score=model_f1_score,
            precision_score=model_precision_score,
            recall_score=model_recall_score
        )
        
        return classification_metric
    except Exception as e:
        raise NetworkSecurityException(e, sys)