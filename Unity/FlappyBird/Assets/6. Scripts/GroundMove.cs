using UnityEngine;

public class GroundMove : MonoBehaviour
{
    public float distance = 7.67f;
    public int index;
    public GameObject[] grounds;
    public Vector3 offSetVector;
    public float nextPosition;
    public float speed;
    
    private Transform _playerTransform;
    
    void Start()
    {
        speed = -0.01f;
        _playerTransform = GetComponent<Transform>();
        offSetVector = new Vector3(speed, 0, 0);
        nextPosition = distance;
    }

    void Update()
    {
        if (Time.timeScale == 0)
            return;

        _playerTransform.localPosition += offSetVector * Time.timeScale;

        if (nextPosition < -_playerTransform.localPosition.x)
        {
            nextPosition = -_playerTransform.localPosition.x + distance;
            grounds[index].transform.localPosition = new Vector3(nextPosition, -5, 0);
            index = (int)Mathf.Repeat(index + 1, 3);
        }
    }

    public void ChangeSpeed()
    {
        speed -= 0.001f;
        offSetVector = new Vector3(speed, 0, 0);
    }
}
