using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using myBehaviourTree;

public class EnemyState_Patrol_Rotation : btAction
{
    private GameObject _myOwner;

    private float _fIntervalTime = 1.0f;
    private Vector3 _vDirection;

    public EnemyState_Patrol_Rotation(GameObject myOwner)
    {
        _myOwner = myOwner;
    }

    public override void Initialize()
    {
        InitDirection();
        SetStateColor();
    }

    private void SetStateColor()
    {
        _myOwner.GetComponent<MeshRenderer>().material.color = Color.green;
    }

    public override void Terminate()
    {
        base.Terminate();
    }

    public override enStatus Update()
    {
        OnRotationByDir();
        return enStatus.Running;
    }

    private void InitDirection()
    {
        float fX = Random.Range(-1.0f, 1.0f);
        float fZ = Random.Range(-1.0f, 1.0f);

        _vDirection = new Vector3(fX, 0.0f, fZ);
        _vDirection.Normalize();
    }

    public void OnRotationByDir()
    {
        _fIntervalTime = _fIntervalTime * Time.deltaTime;
        if (_fIntervalTime < 0.0f)
        {
            float fX = Random.Range(-1.0f, 1.0f);
            float fZ = Random.Range(-1.0f, 1.0f);

            // 예외처리
            if (fX == 0.0f && fZ == 0.0f)
                fX = 1.0f;

            _vDirection = new Vector3(fX, 0.0f, fX);

            // interval 재설정
            _fIntervalTime = Random.Range(0.5f, 3.0f);
        }

        // 회전
        _myOwner.transform.rotation = Quaternion.Slerp(_myOwner.transform.rotation, Quaternion.LookRotation(_vDirection), Time.deltaTime);
    }
}