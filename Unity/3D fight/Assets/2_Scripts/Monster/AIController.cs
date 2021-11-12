using System;
using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;
using UnityEngine.AI;


[RequireComponent(typeof(NavMeshAgent))]
[RequireComponent(typeof(Sensor))]
[RequireComponent(typeof(AIFSM))]
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
    public Vector3[] wanderPoints;
    public int curWanderIndex;
    public NavMeshAgent _navMeshAgent;

    public Vector3 CurrentWanderPoint => wanderPoints[curWanderIndex];
    public bool IsFindTarget => _sensor.currentFindTargets.Count > 0;
    public FindPlayerInfo NearFindPlayer => _sensor.currentFindTargets[0];

    private AIFSM _fsm;
    private Sensor _sensor;
    
    private void Awake()
    {
        _fsm = GetComponent<AIFSM>();
        _navMeshAgent = GetComponent<NavMeshAgent>();
        _sensor = GetComponent<Sensor>();
    }

    private void OnDrawGizmos()
    {
        Handles.color = Color.blue;
        for (int i = 0; i < wanderPoints.Length; i++)
        {
            wanderPoints[i] = Handles.PositionHandle(wanderPoints[i], Quaternion.identity);
            Handles.DrawLine(wanderPoints[i], wanderPoints[(int)Mathf.Repeat(i + 1, wanderPoints.Length)], 2f);
        }
    }

    // private void Update()
    // {
    //     if (_sensor.currentFindTargets.Count > 0)
    //     {
    //         _navMeshAgent.SetDestination(_sensor.currentFindTargets[0].player.transform.position);
    //     }
    // }
}
