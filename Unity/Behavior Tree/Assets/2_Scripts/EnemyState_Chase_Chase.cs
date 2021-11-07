using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using myBehaviourTree;

public class EnemyState_Chase_Chase : btAction
{
    private GameObject _myOwner;

    private float _fSpeedPower = 5.0f;

    public EnemyState_Chase_Chase(GameObject myOwner)
    {
        _myOwner = myOwner;
    }

    public override void Initialize()
    {
        SetStateColor();
    }

    private void SetStateColor()
    {
        _myOwner.GetComponent<MeshRenderer>().material.color = Color.cyan;
    }

    public override void Terminate()
    {
    }

    public override enStatus Update()
    {
        OnChase();
        return enStatus.Running;
    }

    private void OnChase()
    {
        GameObject player = GameObject.FindGameObjectWithTag("Player");
        if (player)
        {
            Vector3 vDir = player.transform.position - _myOwner.transform.position;

            //회전
            _myOwner.transform.rotation = Quaternion.Slerp(_myOwner.transform.rotation, Quaternion.LookRotation(vDir), Time.deltaTime * 4.0f);
            //이동
            _myOwner.transform.Translate(Vector3.forward * _fSpeedPower * Time.deltaTime);
        }
    }
}