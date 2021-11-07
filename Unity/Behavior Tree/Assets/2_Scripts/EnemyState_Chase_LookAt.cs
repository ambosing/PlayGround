using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using myBehaviourTree;

public class EnemyState_Chase_LookAt : btAction
{
    private GameObject _myOwner;

    public EnemyState_Chase_LookAt(GameObject myOwner)
    {
        _myOwner = myOwner;
    }

    public override void Initialize()
    {
        SetStateColor();
    }

    public override void Terminate()
    {
    }

    private void SetStateColor()
    {
        _myOwner.GetComponent<MeshRenderer>().material.color = Color.yellow;
    }

    public override enStatus Update()
    {
        OnLookAt();

        return enStatus.Running;
    }

    private void OnLookAt()
    {
        GameObject player = GameObject.FindGameObjectWithTag("Player");
        if (player)
        {
            Vector3 vDir = player.transform.position - _myOwner.transform.position;

            //회전
            _myOwner.transform.rotation = Quaternion.Slerp(_myOwner.transform.rotation, Quaternion.LookRotation(vDir), Time.deltaTime * 4.0f);
        }
    }
}