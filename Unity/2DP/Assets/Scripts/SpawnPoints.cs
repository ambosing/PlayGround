using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class SpawnPoints : MonoBehaviour
{
    public List<SpawnPoint> spawnPointList = new List<SpawnPoint>();
    public SpawnPoint curSpawnPoint;

    private void Awake()
    {
        GetComponentsInChildren<SpawnPoint>(spawnPointList);
        Debug.Log(spawnPointList[0]);
        curSpawnPoint = spawnPointList[0];
    }
}
