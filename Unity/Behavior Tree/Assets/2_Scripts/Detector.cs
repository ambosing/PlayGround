using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Detector : MonoBehaviour
{
    public Collider[] colliders;
    // Start is called before the first frame update
    void Start()
    {
        colliders = new Collider[1];
    }

    // Update is called once per frame
    void Update()
    {
        Physics.OverlapSphereNonAlloc(transform.position, 7f, colliders, LayerMask.GetMask("Water"));
     
        colliders[0].GetComponent<Parent>().Action();
            
    }
}
