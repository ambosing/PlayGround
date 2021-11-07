using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using myBehaviourTree;

public class EnemyState_Patrol_WayPoint : btAction
{
    private GameObject _myOwner;

    private float _fSpeedPower = 3.0f;

    //waypoint
    private List<Vector3> _listWayPoint = new List<Vector3>();
    private int _iCurrentWayPoint = 0;
    private float _fWayPointRadius = 2.0f;

    public EnemyState_Patrol_WayPoint(GameObject myOwner)
    {
        _myOwner = myOwner;
    }

    public override void Initialize()
    {
        AddWayPoint();
    }

    public override void Terminate()
    {
    }

    public override enStatus Update()
    {
        OnMove();

        return enStatus.Running;
    }

    private void AddWayPoint()
    {
        _listWayPoint.Add(new Vector3(-10.0f, 0.0f, 20.0f));
        _listWayPoint.Add(new Vector3(10.0f, 0.0f, 20.0f));
    }

    private void OnMove()
    {
        Vector3 vWayPoint = _listWayPoint[_iCurrentWayPoint];

        float fDistance = Vector3.Distance(vWayPoint, _myOwner.transform.position);
        // next way point
        if (fDistance < _fWayPointRadius)
        {
            if (++_iCurrentWayPoint >= _listWayPoint.Count)
                _iCurrentWayPoint = 0;
            vWayPoint = _listWayPoint[_iCurrentWayPoint];
        }
        Vector3 vDir = vWayPoint - _myOwner.transform.position;
        //회전
        _myOwner.transform.rotation = Quaternion.Slerp(_myOwner.transform.rotation, Quaternion.LookRotation(vDir), Time.deltaTime * 4.0f);
        //이동
        _myOwner.transform.Translate(Vector3.forward * _fSpeedPower * Time.deltaTime);
    }


}