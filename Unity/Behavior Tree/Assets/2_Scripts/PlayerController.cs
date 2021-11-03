using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public float _fSpeedPower = 10.0f;

    private void Update()
    {
        Move();
    }

    private void Move()
    {
        float fHorizontal = Input.GetAxis("Horizontal");
        float fVertical = Input.GetAxis("Vertical");

        if (fHorizontal == 0.0f && fVertical == 0.0f)
            return;
        Vector3 vMovement = new Vector3(fHorizontal, 0.0f, fVertical);
        transform.rotation = Quaternion.LookRotation(vMovement);
        transform.position += 
            (vMovement.normalized * _fSpeedPower * Time.deltaTime);

    }
}
