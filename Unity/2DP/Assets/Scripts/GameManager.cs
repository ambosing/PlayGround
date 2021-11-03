using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Cinemachine;

public class GameManager : MonoBehaviour
{
    public static GameManager Instance;
    public SpawnPoints spawnPoints;
    public int idx;
    public bool isGameClear;

    private int gameScore = 0;
    private GameObject charPrefab;
    private CinemachineVirtualCamera _virtualCamera;


    private void Awake()
    {
        if (Instance == null)
            Instance = this;
        else if (Instance != this)
        {
            Destroy(this.gameObject);
        }
        spawnPoints = FindObjectOfType<SpawnPoints>();
        _virtualCamera = FindObjectOfType<CinemachineVirtualCamera>();
        charPrefab = Resources.Load("Character") as GameObject;
    }

    private void Start()
    {
        idx = Random.Range(0, 3);
        SpawnCharacter(spawnPoints.spawnPointList[idx].transform);
    }

    public void AddGameScore(int addValue)
    {
        gameScore += addValue;
        UIManager.Instance.SetScoreText(gameScore);
    }

    public int GameScore
    {
        get
        {
            return gameScore;
        }
        set
        {
            gameScore = value;
            UIManager.Instance.SetScoreText(gameScore);
        }
    }

    private void SpawnCharacter(Transform spawnPoint)
    {
        GameObject charObj = Instantiate(charPrefab);
        charObj.transform.position = spawnPoint.position;
        _virtualCamera.Follow = charObj.transform;

        // 시네머신 내의 body, aim쪽의 데이터를 변경하거나 참조하려면
        // GetCinemachineComponent를 활용해야합니다.

    }

    public void Clear()
    {
        isGameClear = true;
        UIManager.Instance.clearUI.Open();
    }
}
