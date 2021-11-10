using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CubeMove : MonoBehaviour
{
    
    float inputX;
    float inputY;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {

        inputX = -Input.GetAxis("Horizontal");
        inputY = -Input.GetAxis("Vertical");
        transform.position += new Vector3(inputX * Time.deltaTime * 5f, 0f, inputY * Time.deltaTime * 5f);
    }
}
