using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class UIManager : MonoBehaviour
{
    public static UIManager Instance;
    public ClearUI clearUI;
    public Text scoreText;

    private void Awake()
    {
        Instance = this;   
    }

    public void SetScoreText(int score)
    {
        scoreText.text = $"Score : {score}";
    }

}
