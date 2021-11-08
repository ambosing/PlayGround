using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MyCameraController : MonoBehaviour
{
    public Transform follower;
    
    [Header("Key Setting")]
    public string horizontalInput = "Mouse X";
    public string verticalInput = "Mouse Y";
    public string zoomInput = "Mouse ScrollWheel";
    public bool isRotateNeedRightClick = true;
    public float currentDistance;

    public float xSpeed = 50f;
    public float ySpeed = 200f;

    [Header("Limit")]
    public float yMinLimit;
    public float yMaxLimit;
    public float distanceMin;
    public float distanceMax;
    
    private float currentAnlgeX;
    private float currentAnlgeY;

    // 초기 카메라 포지션, 회전 값을 기준으로 삼고
    // 유저의 입력에 따라 변화량을 처리해주는 형태로 카메라 회전을 구현
    
    private void Start()
    {
        currentAnlgeX = transform.eulerAngles.y;
        currentAnlgeY = transform.eulerAngles.x;

    }
    
    private void LateUpdate()
    {
        if (!follower)        
        {
            Debug.Log("따라갈 타겟이 없음");
            return;
        }
        if (isRotateNeedRightClick &&  Input.GetMouseButton(1) || !isRotateNeedRightClick)
        {
            currentAnlgeX += Input.GetAxis(horizontalInput) * xSpeed * currentDistance * Time.deltaTime;
            currentAnlgeY -= Input.GetAxis(verticalInput) * ySpeed *Time.deltaTime;

            currentAnlgeY = ClampCameraAngle(currentAnlgeY, yMinLimit, yMaxLimit);
        }

        Quaternion rotation = Quaternion.Euler(currentAnlgeY, currentAnlgeX, 0f);

        float dist = Vector3.Distance(follower.position, transform.position);
        currentDistance = Mathf.Clamp(currentDistance - Input.GetAxis(zoomInput) * dist,
                                        distanceMin,
                                        distanceMax);

        Vector3 pos = follower.position - rotation * new Vector3(0f, 0f, currentDistance);

        transform.position = pos;
        transform.rotation = rotation;
    }

    private float ClampCameraAngle(float anlge, float min, float max)
    {
        if (anlge < -360f)
            anlge += 360f;

        if (anlge > 360f)
            anlge -= 360f;
        
        return Mathf.Clamp(anlge, min, max);
    }
    
}
