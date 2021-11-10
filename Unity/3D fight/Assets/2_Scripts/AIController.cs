using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;


[Serializable]
public class FindPlayerInfo
{
    [SerializeField, ReadOnly] private float lastFindTime;
    public Player player;

    public FindPlayerInfo(Player player)
    {
        this.player = player;
        lastFindTime = Time.time;
    }
    
    /// <summary>
    /// 마지막으로 본 시간 업데이트
    /// </summary>
    public void UpdateFindTime()
    {
        lastFindTime = Time.time;
    }

    /// <summary>
    /// 잊혀져야 하는지 체크
    /// </summary>
    public bool CheckExpire(float forgetTime)
    {
        return (Time.time - lastFindTime) >= forgetTime;
    }
}
public class AIController : MonoBehaviour
{
    private NavMeshAgent _navMeshAgent;
    private Sensor _sensor;
    private void Awake()
    {
        _navMeshAgent = GetComponent<NavMeshAgent>();
        _sensor = GetComponent<Sensor>();
    }

    private void Update()
    {
        if (_sensor.currentFindTargets.Count > 0)
        {
            _navMeshAgent.SetDestination(_sensor.currentFindTargets[0].player.transform.position);
        }
    }
}
