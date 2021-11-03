using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour
{
    public GameObject _myPlayer;
    private Vector3 _vPositionOffset;

    private void Start()
    {
        _vPositionOffset = transform.position - _myPlayer.transform.position;
    }

    private void LateUpdate()
    {
        transform.position = Vector3.Lerp(transform.position,
                    _myPlayer.transform.position + _vPositionOffset,
                    Time.deltaTime * 2.0f);
    }
}
